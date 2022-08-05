# Julien's project

[1 - Subject presentation](#subject) <br>
[2 - Get started](#get-started) <br>
&nbsp;&nbsp;&nbsp;&nbsp;[2.1 - Install project](#install-repo-and-dependencies) <br>
&nbsp;&nbsp;&nbsp;&nbsp;[2.2 - Start demo](#start-demo) <br>

### ***Subject :***
|Instructions||
|:--|--:|
|A file named `etl.py` responsible to store on a given JSON, informations about an artist albums|✔️|
|A class `Album` and `AlbumRepository` :<ul><li>returns the albums of a certain artist</li><li>retrieve all albums sorted by the date they were released</li><li>a function to add an album</li><li>full CRUD</li></ul>|✔️✔️✖️✔️✔️|
|A class `User` and `UserRepository` :<ul><li>make an album borrowable by a given user</li><li>retrieve currently borrowed albums</li><li>retrieve top N albums borrowed previously</li></ul>|✔️✔️✖️✖️|
> NB : some files/classes are named differently in my project
> ```bash
> # Project's file structure
>├── README.md
>├── app
>│   ├── Album.py       [equivalent to Album/AlbumRepository]
>│   ├── User.py        [equivalent to User/UserRepository]
>│   ├── data
>│   │   ├── albums/
>│   │   └── users/
>│   ├── etl.py
>│   ├── requirements.txt
>│   └── utils.py
>└── demo.py
> ```


### ***Get started :***

> Python development version : 3.8.8 <br>
> Development system : macOS Big Sur 11.6.6 <br>
> External dependencies : cf. `./app/requirements.tx`


#### Install repo and dependencies
```bash
# Clone repository
cd <desired-repo>
git clone https://github.com/theoprovost/julien .

# Install dependencies
python -m pip install -r ./app/requirements.txt
```

#### Start demo
|option|description|
|--|--|
|`--i`|Sets CLI interactive mode|

```bash
# Interactive and guided mode
python demo.py --i
```