# D3-Challenge-DOMAICA

## Main folder for solution is called: 'D3-Challenge-DOMAICA'

Inside that root folder, we can find 3 files:

- 'index.html' with code for the webpage for the project.
- 'README.md' -> Markdown with project explanation.
- 'README.pptx' -> Powerpoint containing screenshots, explaining process and main images of the outcomes, of webpages and additional details.

And 1 additional folder:

- 'static'

### - Subfolder 'static' contains:

- 'static/data' subfolder which contains a 'data.csv' (data) file with the sample statistical infos collected for the project that will be used to analyze and plot visualizations.
    
- 'static/js' subfolder with and 'app.js' (coding) file invoked from html containing the javascript code.
  
- 'static/css' subfolder which contains 2 files:  'd3Style.css'  and 'style.css'. Both files are .css Cascading Style Sheets used to adapt the presentation of webpage by modifying and enhancing colors, layouts, margin, fonts, etc.


### - Cross-origin resource sharing (CORS)

 CORS is a mechanism that restricts access to resources on a web page being requested from another domain outside the domain from which the first resource was served.
 
This project has been done by accessing the folder where "index.html" was located with command prompt, activate python and run the command 'python -m http.server'. This python command allows for separating Python code implementing an application’s logic from the HTML (or other) output that it produces. Therefore it lets us to work avoiding CORS security checks.

After running that command, you can access your webpage by browsing in 'localhost:8000' and see the results of your html and js development.

