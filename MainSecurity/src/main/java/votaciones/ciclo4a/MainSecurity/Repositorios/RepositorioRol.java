package votaciones.ciclo4a.MainSecurity.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import votaciones.ciclo4a.MainSecurity.Modelos.Rol;

public interface RepositorioRol extends MongoRepository<Rol, String> {
}
