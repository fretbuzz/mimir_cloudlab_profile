echo 'this is a test!'
echo $1

if [ "$1" = "wordpress" ]; then
  echo "it was testtest"
  # deploy_wordpress.py
elif [ "$1" = "eShop" ]; then
  echo "hello"
 # deploy_eshop.sh
elif [ "$1" = "gitlab" ]; then
  echo "hello gitlab"
 # deploy_gitlab.py
elif [ "$1" = "sockshop" ]; then
  echo "hello shockshop"
elif [ "$1" = "drupal" ]; then
  echo "hello drupal"
fi
