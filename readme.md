I'm at tempelte to showing the right question list from db to here

All normal setups are just done. Know the view and templete also working here

Steps to change existing git user on vs code by these steps

    1. In case of your if you want to change your remote access from one user to another so it's go by changing on you vs code the git global user name and email by running this cmd -> git config --global user.name "yourname" and same for email
    2. After that chack how many remote you added previously on your localsystem of the project by
        git remote -v which show you all remote repository which you added 

        If you have non used repository here then simply remove this by
        ctrl+shift+p and type git: remove remote 
        After that you show the drop-down of all existing remotes here and remove form here which of those which you don't want
    3. If your new remote repository not yet added on local system then add that by the same way and commit fisrt change to check it's working or not