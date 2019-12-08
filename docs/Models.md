Model Architecture

Candidate
    - User          (Foreign key for default User)
    - Fullname
    - Rollnumber
    - Date of Birth
    - Registered Test  (Foreign key for Test)
    - Attempted status
    - Test start time
    - Test end time
    - Score
    - college
    - Aggregate
    - Year
    - Semester
   
    
Test
    - Slug
    - Title
    - password
    - Duration
    - Questions(Many to Many field)
    - Active (bool)

Questions
    - Slug
    - Title
    - Cateogory
    - Level
    - Sampleinput
    - Sampleoutput
    - inputfiles
    - outputfiles

    
