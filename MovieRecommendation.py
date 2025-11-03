from graphviz import Digraph

# Create a use case diagram using Graphviz
dot = Digraph("MetroEvents_UseCase", format="png")
dot.attr(rankdir="LR", size="8")

# Define styles
dot.attr("node", shape="ellipse", fontsize="10")

# Actors
dot.node("User", shape="actor")
dot.node("Organizer", shape="actor")
dot.node("Admin", shape="actor")

# User Use Cases
dot.node("RegisterLogin", "Register/Login")
dot.node("ViewEvents", "View Events")
dot.node("JoinRequest", "Request to Join Event")
dot.node("ReviewEvent", "Review Event")
dot.node("UpvoteEvent", "Upvote Event")
dot.node("ReceiveNotif", "Receive Notifications")

# Organizer Use Cases
dot.node("CreateEvent", "Create Event")
dot.node("EditEvent", "Edit Event")
dot.node("CancelEvent", "Cancel Event")
dot.node("ManageRequests", "Manage Join Requests")

# Administrator Use Cases
dot.node("ApproveOrganizer", "Approve Organizer Request")
dot.node("ManageUsers", "Manage Users")
dot.node("ManageEvents", "Manage Events")
dot.node("OverseeNotif", "Oversee Notifications")

# Associations - User
dot.edge("User", "RegisterLogin")
dot.edge("User", "ViewEvents")
dot.edge("User", "JoinRequest")
dot.edge("User", "ReviewEvent")
dot.edge("User", "UpvoteEvent")
dot.edge("User", "ReceiveNotif")

# Associations - Organizer
dot.edge("Organizer", "CreateEvent")
dot.edge("Organizer", "EditEvent")
dot.edge("Organizer", "CancelEvent")
dot.edge("Organizer", "ManageRequests")

# Associations - Admin
dot.edge("Admin", "ApproveOrganizer")
dot.edge("Admin", "ManageUsers")
dot.edge("Admin", "ManageEvents")
dot.edge("Admin", "OverseeNotif")

# Show inheritance (Organizer is a specialized User)
dot.edge("Organizer", "User", arrowhead="none", style="dashed", label="inherits")

# Render the diagram
file_path = "/mnt/data/MetroEvents_UseCase"
dot.render(file_path)

file_path + ".png"