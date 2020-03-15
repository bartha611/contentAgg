export interface article {
  title: string;
  url: string;
}

export interface websites {
  name: string;
  category: string;
  articles: article[];
}
