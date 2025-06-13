environment = ["dev", "test", "prod", "prod"]
print(environment[1]) 
print(environment.count("prod")) 
environment.append("infra") 
print(environment.append.__doc__) #check the infromation about the append method

def check_environment(env):
    if env == "dev":
        print("Development environment")
    elif env == "test":
        print("Testing environment")
    elif env == "prod":
        print("Production environment")
    else:
        print("Unknown environment")
        check_environment("dev")
# check the environment
check_environment("test")
check_environment("prod")
check_environment("dev")
check_environment("staging")
