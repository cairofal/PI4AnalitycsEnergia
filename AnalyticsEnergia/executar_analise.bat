@echo off
echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Executando analise de potencial energetico...
python analise_potencial_energetico.py

echo.
echo Pressione qualquer tecla para fechar...
pause
