echo 'this is a test!'
echo $1

echo "see, it kinda worked" >> /local/repository/deploy_test_prior.txt
echo "$1" >> /local/repository/deploy_test_prior_val.txt

if [ "$1" = "wordpress" ]; then
  echo "it was testtest"
  echo "see, it was wordpress" >> /local/repository/deploy_test.txt
  # deploy_wordpress.py
elif [ "$1" = "eShop" ]; then
  echo "see, it was eShop" >> /local/repository/deploy_test.txt
 # deploy_eshop.sh
elif [ "$1" = "gitlab" ]; then
  echo "see, it was gitlab" >> /local/repository/deploy_test.txt
 # deploy_gitlab.py
elif [ "$1" = "sockshop" ]; then
  echo "see, it was sockshop" >> /local/repository/deploy_test.txt
elif [ "$1" = "drupal" ]; then
  echo "see, it was drupal" >> /local/repository/deploy_test.txt
fi
