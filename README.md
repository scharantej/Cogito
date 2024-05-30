## Flask Application Design to Explore Philosophy Concepts Website

### HTML Files

- **index.html**: The main page of the website. It displays a list of philosophy topics and a navigation bar to the "Explore" page.
- **explore.html**: Allows users to interact with a specific philosophy concept, displaying text, images, or videos.

### Routes

- **home**: Handles the root route ("/") and renders the "index.html" file.
- **explore/<concept_name>**: Takes a concept name as a parameter and renders the "explore.html" file, providing the content for that concept.
- **about**: A simple route that renders an "about.html" page containing information about the website and its creators.