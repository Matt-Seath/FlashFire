import { useTypedSelector } from "../redux/store";

export const getUser = () => {
  const { user } = useTypedSelector((state) => state.user);

  return { user };
};

export const getWatchlists = () => {
  const { watchlists } = useTypedSelector((state) => state.watchlists);
  
  return { watchlists };
};
