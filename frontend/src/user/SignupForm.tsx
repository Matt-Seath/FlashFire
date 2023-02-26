import { FC } from "react";
import { Form } from "react-final-form";
import { TextField } from "mui-rff";
import { Button, Stack } from "@mui/material";
import useAuth from "./useAuth";
import { useSnackbar } from "notistack";
import useEffectUpdate from "../hooks/useEffectUpdate";

// ----------------------------------------------------------------------

interface FormData {
  username: string;
  email: string;
  password: string;
  confirmPassword: string;
}
const initialValues = {
  username: "testy",
  email: "testy@mail.com",
  password: "Testy123",
  confirmPassword: "Testy123",
};

// ----------------------------------------------------------------------

const Signup: FC = ({}) => {
  const { enqueueSnackbar } = useSnackbar();

  const {
    signup,
    request: {
      signup: { status, error, passwordErrors, emailErrors },
    },
  } = useAuth();

  const onSubmit = async (values: FormData) => signup(values);

  const validate = async (values: FormData) => {
    const { username, email, password, confirmPassword } = values;

    if (!username) return { username: "Required field" };

    if (!email) return { email: "Required field" };

    if (!password) return { password: "Required field" };

    if (!confirmPassword) return { confirmPassword: "Required field" };

    if (confirmPassword !== password)
      return { confirmPassword: "Passwords must match" };

    return;
  };

  useEffectUpdate(() => {
    if (status === "failed") {
      passwordErrors?.map((passwordError: string) => {
        enqueueSnackbar(passwordError, { variant: "error" });
      });

      emailErrors?.map((emailError: string) => {
        enqueueSnackbar(emailError, { variant: "error" });
      });

      if (error) {
        enqueueSnackbar(error, { variant: "error" });
      }
    }
  }, [error, passwordErrors, emailErrors]);

  return (
    <Form
      onSubmit={onSubmit}
      initialValues={initialValues}
      validate={validate}
      render={({ handleSubmit }) => (
        <form onSubmit={handleSubmit} noValidate>
          <Stack direction="column" spacing={2} width={300}>
            <TextField
              label="Username"
              name="username"
              type="text"
              size="small"
              autoComplete="off"
            />

            <TextField
              label="Email"
              name="email"
              type="email"
              size="small"
              autoComplete="off"
            />

            <TextField
              label="Password"
              name="password"
              type="password"
              size="small"
              autoComplete="off"
            />

            <TextField
              label="Confirm Password"
              name="confirmPassword"
              type="password"
              size="small"
              autoComplete="off"
            />

            <Button
              type="submit"
              variant="contained"
              size="large"
              sx={{ textTransform: "none" }}
            >
              Sign up
            </Button>
          </Stack>
        </form>
      )}
    />
  );
};

export default Signup;
