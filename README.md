# calledio
> A chat service where you own your data.  
> No data is stored on a calledio-server.

## installation
> run:

    python setup.py install

## Running a server:

    calledio-server

## Running a client:

    calledio-client


## Where are all messages stored?
> all messages are stored in `$HOME/.calledio/`,  
> if you have sent a message to the channel `general` for example,  
> then those messages will be stored in `$HOME/.calledio/general.log`

> To view your messages _live_, you could do:

    tail -f ~/.calledio/general.log
