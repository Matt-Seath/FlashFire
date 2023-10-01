import { useTypedSelector } from "../redux/store";

export const getUser = () => {
  const { user } = useTypedSelector((state) => state.user);

  return { user };
};

export const getWatchlists = () => {
  const { user } = getUser()
  const watchlists = user.watchlists
  
  return { watchlists };
};
