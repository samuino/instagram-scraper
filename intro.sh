
    #!/bin/bash
    echo WELCOME TO INSTAGRAM SCRAPER
    echo LOADING...
    cd /Desktop/instagram-scraper-full
    pip install instagram-scraper
    echo Enter Your User ID :
    read varname
    echo Enter Your Password :
    read pass
    echo Enter the user id you want to scrap
    read user
    instagram-scraper --media-metadata $user -u $varname -p $pass
    
    cp /root/Desktop/instagram-scraper-full/sort.py /root/Desktop/instagram-scraper-full/$user/
    cd $user
    python3 sort.py
