import { faker } from "@faker-js/faker";
import { v4 as uuid4 } from "uuid";
import userFixtures from "./user";

function postFixtures(isLike = true, isEdited = false, user = undefined) {
  return {
    id: uuid4(),
    author: user || userFixtures(),
    body: faker.lorem.sentence(20),
    edited: isEdited,
    liked: isLike,
    likes_count: Math.floor(Math.random() * 10),
    comments_count: Math.floor(Math.random() * 10),
    created: faker.date.recent(),
    updated: faker.date.recent(),
  };
}

export default postFixtures;
