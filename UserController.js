// Boundary class (B) for handling user creation interface

class CreateUserPage {
  constructor() {
    this.controller = new CreateUserController();
    this.initialize();
  }

  // Initialize the UI components and event listeners
  initialize() {
    document.addEventListener('DOMContentLoaded', () => {
      // Initialize form handler
      this.initializeForm();
    });
  }

  // Initialize the user creation form
  initializeForm() {
    const form = document.getElementById('create-user-form');
    if (!form) return;
    
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const userId = document.getElementById('userId').value;
      const password = document.getElementById('password').value;
      
      // Call the controller to create user
      const success = this.createUser(userId, password);
      
      // Show appropriate message
      if (success) {
        this.showMessage('User created successfully', true);
        form.reset();
      } else {
        this.showMessage('Failed to create user', false);
      }
    });
  }

  // Create user via controller
  createUser(userId, password) {
    return this.controller.createUser(userId, password);
  }

  // Show a message in the message container
  showMessage(message, isSuccess) {
    const messageDiv = document.getElementById('message');
    if (!messageDiv) return;
    
    messageDiv.textContent = message;
    messageDiv.className = isSuccess ? 'success' : 'error';
  }
}


// Control class (C) for managing user creation

class CreateUserController {
  constructor() {
    this.userEntity = new User(null, null, null);
  }

  // Boolean function to create user
  createUser(userId, password, email) {
    // Basic validation
    if (!userId || !password) {
      return false;
    }
    
    // Check if user ID is valid
    if (!this.isValidUserId(userId)) {
      return false;
    }
    
    // Create user via entity
    return this.userEntity.createUser(userId, password, email);
  }
  
  // Helper method to validate user ID
  isValidUserId(userId) {
    // Basic validation - in a real application, this would be more robust
    return userId.length >= 3;
  }
}

// Entity class (E) for managing user data and persistence

class User {
  constructor(userId = null, password = null) {
    this.userId = userId;
    this.password = password;
    this.userStore = this.getUserStore(); 
  }

  // Create a new user in the system
  createUser(userId, password) {
    // Set the properties on this instance
    this.userId = userId;
    this.password = this.hashPassword(password); // Store hashed password for security
    
    try {
      // Check if user already exists
      if (this.userExists(userId)) {
        console.error('User already exists');
        return false;
      }
      
      // Save user to storage
      const user = {
        userId: this.userId,
        password: this.password,
        createdAt: new Date().toISOString()
      };
      
      // Add to user store (Sampled data structure)
      this.userStore.push(user);
      
      // Persist to storage
      this.saveUserStore();
      
      return true;
    } catch (error) {
      console.error('Error creating user:', error);
      return false;
    }
  }
  
  // Check if a user with the given ID already exists
  userExists(userId) {
    return this.userStore.some(user => user.userId === userId);
  }
  
  // Get all users from the store
  getAllUsers() {
    return this.userStore;
  }
  
  // Hash password for secure storage
  hashPassword(password) {
    // This is a placeholder for a real hashing function
    return `hashed_${password}_${Date.now()}`;
  }
  
  // Get user store from local storage or initialize if not exists
  getUserStore() {
    try {
      const storeJson = localStorage.getItem('userStore');
      return storeJson ? JSON.parse(storeJson) : [];
    } catch (error) {
      console.error('Error loading user store:', error);
      return [];
    }
  }
  
  // Save user store to local storage
  saveUserStore() {
    try {
      localStorage.setItem('userStore', JSON.stringify(this.userStore));
    } catch (error) {
      console.error('Error saving user store:', error);
    }
  }
  
  // Find a user by ID
  findUserById(userId) {
    return this.userStore.find(user => user.userId === userId);
  }
  
  // Authenticate a user
  authenticate(userId, password) {
    const user = this.findUserById(userId);
    if (!user) return false;
    
    // sample
    const hashedInput = this.hashPassword(password);
    return user.password === hashedInput;
  }
}
