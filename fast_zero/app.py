from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello World'}


'''
@app.post('/batata')
def read_batata():
    return {'message': 'Batatas fritas são saudáveis'}


@app.post('/suco')
def read_suco():
    return {'message': 'Beba suco de abacate'}
'''
