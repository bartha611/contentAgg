export interface article {
  title: string;
  url: string;
}

export interface website {
  id: number;
  name: string;
  category: string;
  clicks: number;
  articles: article[];
}
