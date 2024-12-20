class Registro_Usuario():
    def __init__(self,  num_doc:int ,nom_ape:str , usuario:str, clave:str, rol:str):
        self._num_doc= num_doc
        self._nom_ape = nom_ape
        self._usuario = usuario
        self._clave = clave
        self._rol = rol