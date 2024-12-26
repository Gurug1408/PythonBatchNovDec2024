import argparse

parser = argparse.ArgumentParser(
    description="Details to login to server", 
    epilog="-----Please follow help doc ----"
)
# description: for the text that is shown before the help text
# epilog: for the text shown after the help text

parser.add_argument("-u", "--username", help="login user name", type=str, required=True)
parser.add_argument(
    "-p", "--password", help="login user password", type=str, required=True
)
parser.add_argument(
    "-s",
    "--servername",
    help="server name",
    type=str,
    required=False,
    default="www.google.com",
)

args = parser.parse_args()

user_name = args.username
password = args.password
server_name = args.servername

print(
    f"""
The server login details are:
    USER NAME   : {user_name}
    PASSWORD    : {password}
    SERVER NAME : {server_name}
"""
)