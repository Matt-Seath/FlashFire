import { useTypedSelector } from "../redux/store";

export const getUser = () => {
  const { user } = useTypedSelector((state) => state.user);

  return { user };
};
