import React, { FC, ReactElement } from "react";
import { Box, Container, Grid, Typography } from "@mui/material";

export const Footer: FC = (): ReactElement => {
  return (
    <Box
      sx={{
        position: "fixed",
        bottom: 0,
        width: "100%",
        height: 50,
        backgroundColor: "#020409",
        paddingTop: "0.9rem",
        paddingBottom: "0.7rem",
      }}
    >
      <Container maxWidth="lg">
        <Typography
          sx={{ textAlign: "center", color: "grey", fontSize: "0.9rem" }}
        >
          © 2023 Copyright: Matthew Seath
        </Typography>
      </Container>
    </Box>
  );
};

export default Footer;
