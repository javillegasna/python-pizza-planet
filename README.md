<h1 align="center"> Python Pizza Planet </h1>

![python-badge](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

This is an example software for a pizzeria that takes customizable orders.

## Table of Contents

- [Getting started](#getting-started)
- [Running the backend project](#running-the-backend-project)
- [Running the frontend](#running-the-frontend)
- [Testing the backend](#testing-the-backend)

## Getting started

You will need the following general tools:

- A Python interpreter installed. [3.8.x](https://www.python.org/downloads/release/python-3810/) is preffered.

- A text editor: preferably [Visual Studio Code](https://code.visualstudio.com/download)

- Extensions such as [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

## Running the backend project

- Clone the repo

```bash
git clone https://github.com/ioet/python-pizza-planet.git
```

- Create a virtual environment in the root folder of the project

```bash
make create_environment
```

- Activate the virtual environment (In vscode if you select the virtual env for your project it will activate once you open a new console window)

_For linux/MacOS users:_

```bash
source .venv/bin/activate 
```

_For windows users:_

```cmd
\path\to\env\Scripts\activate
```

- Install all necessary dependencies:

```bash
make install
```

- Start the database (Only needed for the first run):

```bash
make start_database
```

- Start the server

```bash
make start_server
```

- Start the server whit hot reload

```bash
make start_server_hot_reload
```

- Execute test lint

```bash
make run_lint
```

- Execute test

```bash
make run_tests
```

- If you want to use the hot reload feature set FLASK_ENV before running the project:

_For linux/MacOS users:_

```bash
export FLASK_ENV=development 
```

_For windows users:_

```CMD
set FLASK_ENV=development
```

- Run the project with:

```bash
python3 manage.py run
```

## Running the frontend

- Clone git UI submodule

```bash
git submodule update --init
```

- Install Live Server extension if you don't have it from [here](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) on VSCode Quick Open (`Ctrl + P`)

```bash
ext install ritwickdey.LiveServer
```

- To run the frontend, start `ui/index.html` file with Live Server (Right click `Open with Live Server`)

- **Important Note** You have to open vscode in the root folder of the project.

- **To avoid CORS errors** start the backend before the frontend, some browsers have CORS issues otherwise

### Testing the backend

- Make sure that you have `pytest` installed

- Run the test command

```bash
python3 manage.py test
```
## Pizza-Planet-Deploy

![Pizza-Planet-Deploy](http://www.plantuml.com/plantuml/svg/hLPjRzis4FwkNt4H0ZG18cl9-YdmWkPjgO4KDUmM_LAWeAYBJ8GY1PAAwmxvxpkIiYHdSJ0C4mn9l7kUu_7Uv0_MCUFQMi9S_Fh5ihba2brsWutKcoHv1quuYQyf9_1HLAjCuXDAO8QlX4FkMeDG2bOPLYS79Ju8XN3vRJdtEwoSQ-nvdXksdbJ2hTgYjMYuLWwLct1Tvsnj9IkiVsQ253Pxq2PhQ5llOlvq-dxoMruAwv83eRXiozvuJizhNTTQJHfQ_bD_mnmhcCLySRFS0xb3XOR9_2jvjGzYTDlOi9dKRVasAjWJ_4gsk0T87ZUjm_oUrKN9ultFLd4dzfxZ4rEimfeYTgUVq2YcEER1cM_CyTKUrcNJIC6PjpkZS5Dw_6j-EP_TCOThjjdhe7ACScXiVYkPTOBtaWLMb0Yp-Mz-tklAxc4kaRT6kCsi938zVP2a2Fojw99pj7ROOg5b5-A-w9RpnUpBxVBhulvVrDssmZBhIYcAl1AoO8P-B1jK3Jc5begGQh1RzCwtHevsp4lD7r_Mq0k8GsCOLNVz9Ygw6teXujv1B2xgE0H33STK9T72ce30WBVMwHgisr3JjbQeYjxHe7QR1Y43XLY2qx0I9IR-Db8dzb6eXivSWwG81eOsRgL7Ydv7-2i1kguOVwp88LLUQwcDp-6FgxiVrv_lFoyYG9iIJLGwmvGbEnJre5kkMAdNtiS79YqcpvIzncYEfPyYXsHhHkS-EgHaFGcE9t3e_JhjdcT_fEbnCZYK1a9TzVZZxsfQN4JED2yklgl8IvC3LEMmqOI2klRJ2np-T20KnR6GT30ezCyTZoXMZMhheqEw5MYE8PaMX3iFw8ifzwSy3wOkQ6VeOE0td-P1Iq_F85zsdKZewW_ivyy9f93IpR-dny0i-9eT7tTws9SGcGFQyCjs3V6uC0ZYo4wzdPvr-hzQEzkr5ZkWCtNL2bbsPW8hQfFj60qbVSJzwx6lgpuI-sOE1URsUf6688NW83TZtZ1d218MQxyO4RXSZmcl3M0FzXTX86feCJ8XWsniPHYd7PS4q4bWbymQKOsfRqsspjZiyXFufNrXIj2dzjMp-ndRSGSXI9A-i4318EdO27qaEoQzlK2RqX9qA2F8J7RXCt0-T4XwIhq9NPu3O2YKCUpt01jqa96f6DWnx7s0qHQGbGI8PiU0im7G4Y1cDze99gF01prw6zTqx_4n02DAbw6jnCDYfCUI60lVcd4TICzxUhdqVvLqisteVfcC_YZ4LeXZ_oIz4-vZMwIXANRQQ_HTw7giax1GkZOqMsYrQiLsoVE5_m3Kr4z1xqD8089beoITHX5CisoBwDqD9mt2v-G33J7wBFqD "Pizza-Planet-Deploy")

## Pizza-Planet-UI-Deploy

![Pizza-Planet-UI-Deploy](http://www.plantuml.com/plantuml/svg/dLLjQzim4FxkNt4rWJLGnzlOfvA5jTtM1LeMafL-6HHPkjgYicGakLawzjztaft4xTOoPaBaUtdk_UGFpZFhsrh1GZuyi6oXc4QVNSspZzWeiqcIL-2bL_YCV09VP5bb2kzH0REyaXwvRos2aAoqh4uE1DvAZN1olLe4FvNtZJlESylMarBwgYrQXvORxL7x2JTrpjPEiSA5CvCaSDcjiLb3daEW-VsRTvFNkP3E9mTISzMAdV6SpZDJrqPF6YB_b9-ZHijKVaKkdrEnfcrSjAHCArxMYlOaFrKjFgDuoJGhiQRSpiqzMiqqnpnQlcQUL_-7kZ2bUmQvGjvQwJTpGM0wgHoDaX6_PPrmZixjNIoDwgF_qzndIutvfCKr5fUca0hpas3lTjExxvkxMYpdtpwjhfON_z3VRISpvuMIHLvALJ1BFvRjHGqbWOwQJRtkYLrqhLK3Zxam_EvfEv-eUBIMqHJLBsfruSQPw_HUGTTdccm4IuFDTAdGmPeKWG5ldJSrEB-X_MYTr2MzeqNZDmr21XfHW3TGIO59-1k84tSdTKCvrw2eWX5XhA_CGB3p23yJeEUKyRkI0jBYp2XZGvDkJizlphvUV5rs2iOAj9tGMwOTsQ6gHzcgOiAiGuotJ3bCVb6t6siuYh2j8x8rfxmFHzIiUydn24OXhZVz-VPzcewJVK1f1DJbJd_yNK-BMOUPviNik-vmQNA0MkmTJQYewt1BWCSV7gIcEXQA4eF2_7WK4TMgqMrzEAA_0kqOacb1UiTHUpRb8SlZQ6f6dg5NW-1ycaSfdG51iJmE8g5dbt2u2euWXPJ-mdiw1kOWp6oIR2-1E0M7FBoEGojsuFrA4ZeIwq2aqM0qnDLw2EYtP-kGsD2pEdNM4N_t4TO-8EdPCq4HDx0UEoNkqCXBkz-Rd9zSGY2V6fDqYSCsCCYoMP_JaDFf43zGlVSmON-jiWWV2zDiIxqZay5jsbMyMyYRLXwbvz9_QOkdNw4qjcCmbejbMBYQIPq6ss667YjCHuCjfya0cfsUmxYNzBM94nJHPSKIGjD1MUqxGpHCisnhV1S_P6qswvbXVc20-fLye0caE-Kt "Pizza-Planet-UI-Deploy")