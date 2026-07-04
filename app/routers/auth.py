from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix="", tags=["Auth"])
security = HTTPBasic()

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Verifica las credenciales HTTP Basic Auth.
    Usuario: admin, Contraseña: secret
    """
    correct_username = "admin"
    correct_password = "secret"
    
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@router.get("/secure/")
def secure_endpoint(username: str = Depends(verify_credentials)):
    """
    Endpoint protegido con HTTP Basic Auth.
    
    Requiere:
    - Usuario: admin
    - Contraseña: secret
    
    Retorna un mensaje de bienvenida si las credenciales son correctas.
    """
    return {"message": f"Bienvenido {username}, has accedido al endpoint seguro"}