import unittest
from unittest.mock import patch, MagicMock
import asyncio
from heartbeat import registrar_latido_async

class TestWatchdogIntegridad(unittest.IsolatedAsyncioTestCase):
    """Arnés de pruebas asíncronas con soporte para lectura en bloques."""

    async def test_integridad_exitosa(self) -> None:
        """TEST 1: Caso de éxito simulando lectura por bloques en RAM."""
        # Hash SHA-256 exacto y verificado de b"bytes_correctos_simulados"
        hash_falso = (
            "5d0c638f04f583e296c823ff8be164aef77d3c5d4a5558f3b69f84ef6daa4673"
        )

        # Fabricamos un simulador de archivo manual que entiende el bucle while
        mock_file = MagicMock()
        # Primera llamada devuelve los bytes; segunda llamada devuelve vacío para romper el bucle
        mock_file.read.side_effect = [b"bytes_correctos_simulados", b""]
        
        # Configuramos el administrador de contexto (with open)
        mock_open_context = MagicMock()
        mock_open_context.__enter__.return_value = mock_file

        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", return_value=mock_open_context):
                with patch("heartbeat.FIRMA_ESPERADA", hash_falso):
                    with patch("heartbeat.asyncio.to_thread"):
                        await registrar_latido_async()

    async def test_integridad_fallida(self) -> None:
        """TEST 2: Caso de ataque con bytes alterados."""
        mock_file = MagicMock()
        mock_file.read.side_effect = [b"bytes_ataque_corruptos", b""]
        
        mock_open_context = MagicMock()
        mock_open_context.__enter__.return_value = mock_file

        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", return_value=mock_open_context):
                with self.assertRaises(SystemExit):
                    with patch("heartbeat.registrar_alerta") as mock_alerta:
                        await registrar_latido_async()
                        mock_alerta.assert_called_once()
