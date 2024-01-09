#!/bin/bash
cd app/static/css
ln -s ../../dependencies/tabler-v1.0.0-beta19/tabler/dist/css/tabler.min.css tabler.min.css
ln -s ../../dependencies/tabler-v1.0.0-beta19/tabler/dist/css/tabler-flags.min.css tabler-flags.min.css
ln -s ../../dependencies/tabler-v1.0.0-beta19/tabler/dist/css/tabler-payments.min.css tabler-payments.min.css
ln -s ../../dependencies/tabler-v1.0.0-beta19/tabler/dist/css/tabler-vendors.min.css tabler-vendors.min.css
ln -s ../../dependencies/tabler-v1.0.0-beta19/tabler/dist/css/demo.min.css demo.min.css

cd ../js
ln -s ../../../dependencies/tabler-v1.0.0-beta19/tabler/dist/js/tabler.min.js tabler.min.js
ln -s ../../../dependencies/tabler-v1.0.0-beta19/tabler/dist/js/demo.min.js demo.min.js