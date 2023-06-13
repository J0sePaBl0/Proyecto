from Usuario import Usuario
from Admin import Admin

def main():

    cliente1 = Usuario(12332,"Dayana", "dayana@gmail.com")
    cliente1.Display()
    jose = Admin(12332,"Jose", "dayana@gmail.com","kdskdfk")
    jose.Display()

if __name__ == '__main__':
    main()