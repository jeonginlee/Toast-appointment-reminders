import asyncio
import configparser
import os
from msgraph.generated.models.o_data_errors.o_data_error import ODataError
from graph import Graph

async def main():
    print("Toast Appointment Reminder",'\n')

    # Loading settings
    config = configparser.ConfigParser()
    config_path = os.path.join(os.getcwd(),'config.cfg')
    config.read(config_path)
    azure_settings = config['azure']

    graph: Graph = Graph(azure_settings)

    await greet_user(graph)

    choice = -1

    while choice != 0:
        print('Please choose one of the following options:')
        print('0. Exit')
        print('1. Display access token')
        print('2. Create appointment reminder')
        print()

        try:
            choice = int(input())
        except ValueError:
            choice = -1

        try:
            if choice == 0:
                print ('See ya')
            elif choice == 1:
                await display_access_token(graph)
            elif choice == 2:
                await create_appointment_reminder(graph)
            else:
                print("Invalid choice\n")
        except ODataError as odata_error:
            print("Error:")
            if odata_error.error:
                print(odata.error.error.code, odata_error.error.message)


async def greet_user(graph: Graph):
    user = await graph.get_user()
    if user:
        print("Hello,", user.display_name, "(" + (user.mail or
        user.user_principal_name) + ")", '\n')
    return

async def display_access_token(graph: Graph):
    token = await graph.get_user_token()
    print('User token:', token, '\n')
    return

async def create_appointment_reminder(graph: Graph):
    # TODO parse OneNote for meeting details
    # TODO call graph to creat event with details
    return


asyncio.run(main())
