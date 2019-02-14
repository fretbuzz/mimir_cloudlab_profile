"""This profile demonstrates a *parameterized profile* that allows you to select one of several standard OS images for your nodes. When you instantiate this profile, you will be asked to select the OS via a drop down menu.

Instructions:
Click on any node in the topology and choose the `shell` menu item."""

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
pc.defineParameter("osImage", "Select OS image",
                   portal.ParameterType.IMAGE,
                   imageList[0], imageList,
                   longDescription="Most clusters have this set of images, " +
                   "pick your favorite one.")

applicationList = [
    ('none', 'none'), ('wordpress', 'wordpress'), ('sockshop','sockshop'), ('drupal','drupal'), ('eShop','eShop'), ('gitlab', 'gitlab'),]

#pc.defineParameter( "Application To Start", "Select App", portal.ParameterType.STRING, applicationList[0],
#                  applicationList, longDescription="Which app to auto start?")
#portal.context.defineParameter( "n", "Number of VMs", portal.ParameterType.INTEGER, 1 )
#imageList = [
#    ('urn:publicid:IDN+wisc.cloudlab.us+image+dna-PG0:minikube_starter:2', 'UBUNTU 16.04'),]
    
# Define a single parameter for the instantiation page.
pc.defineParameter("App", "Select App image",
                   portal.ParameterType.IMAGE,
                   applicationList[0], applicationList,
                   longDescription="Most clusters have this set of images, " +
                   "pick your favorite one.")

# Retrieve the values the user specifies during instantiation.
params = pc.bindParameters()

# Add a raw PC to the request and set the disk image.
node = request.RawPC("node")
node.disk_image = params.osImage

# added an ephemeral blockstore per documentation instructions
bs = node.Blockstore("bs", "/mydata")
bs.size = "80GB"
bs.placement = "nonsysvol"

node.addService(pg.Execute(shell="bash", command="touch /local/repository/test_test.xt"))
node.addService(pg.Execute(shell="bash", command="bash /local/repository/test_profile_script_running.sh"))
node.addService(pg.Execute(shell="bash", command="chmod +x /local/repository/test_profile_script_running.sh"))
node.addService(pg.Execute(shell="bash", command="/local/repository/test_profile_script_running.sh"))
node.addService(pg.Execute(shell="bash", command="bash /local/repository/test_profile_script_running.sh"))

node.addService(pg.Execute(shell="bash", command="chmod +x /local/repository/kubernetes_setup.sh"))
node.addService(pg.Execute(shell="bash", command="/local/repository/kubernetes_setup.sh"))
node.addService(pg.Execute(shell="bash", command="bash /local/repository/kubernetes_setup.sh"))

node.addService(pg.Execute(shell="bash", command="chmod +x /local/repository/deploy_application.sh"))
node.addService(pg.Execute(shell="bash", command="/local/repository/deploy_application.sh " + str(params.App)))
node.addService(pg.Execute(shell="bash", command="bash /local/repository/deploy_application.sh " + str(params.App)))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
