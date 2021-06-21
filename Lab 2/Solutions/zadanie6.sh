#!/bin/bash

echo -n "Sciezka: "
read path

counter(){
    for file in "$1"/* 
    do 
    if [ -d "$file" ]
    then 

            echo  "$file"
            counterhelp "$file" "$2"

    fi
    done
}

counterhelp(){
	for file in "$1"/* 
    do 
    if [ -d "$file" ]
    then 

    		echo -n "$2"
            echo  "$file"
            counterhelp "$file" "$2$2"
    fi
    done
}


counter "$path" "--"
read path
