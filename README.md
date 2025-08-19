## Client Manager

```
# Install pip dependency manager
python get-pip.py --user
pip install faker
```

Bonus:

https://rich.readthedocs.io/en/stable/introduction.html
https://click.palletsprojects.com/en/8.1.x/

### CliManager v1.0

```
**************************
Welcome to CliManager v1.0
**************************

Select the number of your choice to display screen
[1] - Print my clients
[2] - Add a client
[3] - Edit a client
[4] - Delete a client
[5] - Exit
```
#### Generate clients

You can use Faker to generate random clients inside the function `generate_clients`

[Click here for the Faker documentation](https://faker.readthedocs.io/en/master/#basic-usage)

#### Print my clients

```
::::::::::::::::
Print my clients
****************

Select 5 to return to the menu

_______________________________________
| ID | Name | Address | Total spent Â£ |
---------------------------------------
| ...| .... | ........| ..............|
| ...| .... | ........| ..............|
|____|______|_________|_______________|
```

#### Add a client
 
```
::::::::::::::::
Add a client
****************

Select 5 to return to the menu

Name:
>> John Doe
Address :
>> 15 Doughty Court, Stratford Street, London
Total spent Â£ :
>> 200000

!! Client added !!
```

#### Edit a client
 
```
::::::::::::::::
Edit a client
****************

Select 5 to return to the menu

Choose an client ID for updating :
>> 10
[Client found]
Let blank if no change
Address [15 Doughty Court, Stratford Street, London] :
>>
Total spent [200000] :
>> 300000

!! Client updated !!
```

#### Delete a client

```
::::::::::::::::
Delete a client
****************

ID of the client to remove :
>> 10
Client to delete not found
>> 1
Client deleted
```

#### Testing

For each feature, testing is expected to make sure everything is working as defined. (pytest)
 
