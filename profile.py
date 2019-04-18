""" This profile is used to help setup the MIMIR project experimental apparatus. This profile helps setup a Minikube cluster and generate data from microservice applications. Recommended to be used with the run_exp_on_cloudlab.py script from the MIMIR repo."""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context, needed to defined parameters
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

#
# This is a typical list of images.
#
imageList = [
    ('urn:publicid:IDN+wisc.cloudlab.us+image+dna-PG0:minikube_starter:2', 'UBUNTU 16.04'),]
    
# Define a single parameter for the instantiation page.
#pc.defineParameter("osImage", "Select OS image",
#                   portal.ParameterType.IMAGE,
#                   imageList[0], imageList,
#                   longDescription="Most clusters have this set of images, " +
#                   "pick your favorite one.")

#applicationList = [
#    ('none', 'none'), ('wordpress', 'wordpress'), ('sockshop','sockshop'), ('drupal','drupal'), ('eShop','eShop'), ('gitlab', 'gitlab'),]


# Define a single parameter for the instantiation page.
#pc.defineParameter("App", "Select App image",
#                   portal.ParameterType.IMAGE,
#                   applicationList[0], applicationList,
#                   longDescription="Most clusters have this set of images, " +
#                   "pick your favorite one.")

# Retrieve the values the user specifies during instantiation.
params = pc.bindParameters()

# Add a raw PC to the request and set the disk image.
node = request.RawPC("node")
node.disk_image = imageList[0] #params.osImage

# added an ephemeral blockstore per documentation instructions
bs = node.Blockstore("bs", "/mydata")
bs.size = "80GB"
bs.placement = "nonsysvol"

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
