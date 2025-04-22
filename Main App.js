// app.js
// Main application file that initializes the user creation flow

// In a real application with ES modules, you would import the classes
// import User from './user-entity.js';
// import CreateUserController from './user-control.js';
// import CreateUserPage from './user-boundary.js';

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
  // Create the boundary (which will create the controller and entity)
  const createUserPage = new CreateUserPage();
  
  // Log initialization
  console.log('User Creation System initialized');
  
  // For sequence diagram testing
  window.testUserCreationFlow = function(userId, password) {
    console.log('--- Testing User Creation Flow ---');
    console.log(`Inputs: userId=${userId}, password=${password}`);
    
    const boundary = new CreateUserPage();
    const result = boundary.createUser(userId, password);
    
    console.log(`User creation ${result ? 'successful' : 'failed'}`);
    console.log('--- Test Complete ---');
    
    return result;
  };
});