import uvicorn

# ########## App engine ########
if __name__ == "__main__":
    uvicorn.run('Book.app:app', host='127.0.0.1', port=8000, reload=True)
    
