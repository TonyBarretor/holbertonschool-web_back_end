// 100-await.js

import { uploadPhoto, createUser } from "./utils.js";

async function asyncUploadUser() {
    try {
        // Call the uploadPhoto and createUser functions asynchronously
        const [photoResponse, userResponse] = await Promise.all([
            uploadPhoto(),
            createUser()
        ]);

        // Return an object with photo and user responses
        return {
            photo: photoResponse,
            user: userResponse
        };
    } catch (error) {
        // If an error occurs in any of the asynchronous functions, return an empty object
        console.error('An error occurred:', error);
        return {
            photo: null,
            user: null
        };
    }
}

export default asyncUploadUser;
