# calledio
> A chat service where you own your data.  
> No data is stored on a calledio-server.

## Known issues:

    * server is single-threaded (will be fixed soon)

## installation
> create your config file:

    cp config.example.json config.json

> Edit the `config.json` file...

> run:

    python setup.py install

## Running a server:

    calledio-server

## Running a client:

    calledio-client


## Where are all messages stored?
> You specify in the `config.json` where to store messages / channels.  
> if you have sent a message to the channel `general` for example,  
> then those messages will be stored in `$directory/general.log`

> To view your messages _live_, you could do:

    tail -f $directory/general.log
