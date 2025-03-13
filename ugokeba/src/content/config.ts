import { z, defineCollection } from "astro:content";

const snippetsCollection = defineCollection({
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    index: z.number(),
  }),
});

export const collections = {
  snippets: snippetsCollection,
};
