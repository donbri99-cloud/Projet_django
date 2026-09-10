git switch arsene
git add .
git commit -m "Ma fonctionnalité"
git push origin arsene

## Envoyé mes changements dans develop
git switch develop
git pull origin develop

git merge arsene
git push origin develop

git switch arsene


## Pourque Alice reçoit la develop
git status
git switch alice
git pull origin alice
git fetch origin
git merge origin/develop
git status
git push origin alice



## Si conflit
git status

<<<<<<< HEAD
        ↓
Version actuelle = alice

=======

Version venant de develop

>>>>>>> origin/develop

--puis
git add .

git status (Si il n'y a plus conflit)

git commit

git push origin alice