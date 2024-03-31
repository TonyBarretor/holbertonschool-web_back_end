import { uploadPhoto, createUser } from "./utils.js";

async function asyncUploadUser() {
  try {
    const photoResponse = await uploadPhoto();
    const userResponse = await createUser();
    return {
      photo: photoResponse,
      user: userResponse
    };
  } catch (error) {
    console.error("Error:", error);
    return {
      photo: null,
      user: null
    };
  }
}

export default asyncUploadUser;
