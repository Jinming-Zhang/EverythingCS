#!/bin/bash
# VAR1="Wolfy"
# VAR2="Foxy"
# var3="Doggy"
build_dir="personal-react-dev"
tar_dir="$HOME/personal-react-dev"

echo "Updating git directory..."
if [ ! -d $tar_dir ]; then
  cd ~
  $(git clone git@github.com:Jinming-Zhang/personal-react-dev)
fi
cd $tar_dir
