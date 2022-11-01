from Repositorios.PartidoRepositorio import PartidoRepositorio
from Modelos.Partido import Partido

class PartidoControlador():
    #constructor
    def __init__(self):
        self.repositorioPartido = PartidoRepositorio()
    
    #devuelve todos los documentos
    def index(self):
        return self.repositorioPartido.findAll()
    
    #crea documentos
    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)
    
    #muestra un documento
    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__
    
    #actualiza un documento
    def update(self, id, infoPartido):
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)
    
    #borra un documento
    def delete(self, id):
        return self.repositorioPartido.delete(id)