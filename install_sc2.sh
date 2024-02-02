#!/bin/bash
# Install SC2 and add the custom maps

if [ -z "$EXP_DIR_PYMARL" ]
then
    EXP_DIR_PYMARL="$HOME/Repositories"
    export EXP_DIR_PYMARL
fi

echo "EXP_DIR: $EXP_DIR_PYMARL"
cd $EXP_DIR_PYMARL/pymarl

if [ ! -d "3rdparty" ]
then
    mkdir 3rdparty
fi

cd 3rdparty

# only available for the current shell session
export SC2PATH=`pwd`'/StarCraftII'
echo 'SC2PATH is set to '$SC2PATH

if [ ! -d $SC2PATH ]; then
        echo "StarCraftII is not installed in $SC2PATH"

        echo "Checking folder $EXP_DIR_PYMARL/StarCraftII"

        if [ -d "$EXP_DIR_PYMARL/StarCraftII" ]
        then
                echo "StarCraftII found and copied from $EXP_DIR_PYMARL"
                cp -r "$EXP_DIR_PYMARL/StarCraftII" .
        else
                echo 'StarCraftII is not installed. Installing now ...';
                wget http://blzdistsc2-a.akamaihd.net/Linux/SC2.4.10.zip
                unzip -P iagreetotheeula SC2.4.10.zip
                rm -rf SC2.4.10.zip
        fi
else
        echo 'StarCraftII is already installed.'
fi

echo 'Adding SMAC maps.'
MAP_DIR="$SC2PATH/Maps/"
echo 'MAP_DIR is set to '$MAP_DIR

if [ ! -d $MAP_DIR ]; then
        mkdir -p $MAP_DIR

        echo "Maps not found in $MAP_DIR. Downloading now ..."

        cd ..
        wget https://github.com/oxwhirl/smac/releases/download/v0.1-beta1/SMAC_Maps.zip
        unzip SMAC_Maps.zip
        mv SMAC_Maps $MAP_DIR
        rm -rf SMAC_Maps.zip
else
        echo 'Maps are already installed.'
fi



echo 'StarCraftII and SMAC maps installation successful.'