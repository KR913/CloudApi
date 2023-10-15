call conda activate
echo conda activated!

call pip3 install -r requirements.txt

call python -m uvicorn main:app --reload --port=8000

call conda deactivate