import * as React from "react";
import { styled, alpha } from "@mui/material/styles";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import SearchIcon from "@mui/icons-material/Search";
import InputBase from "@mui/material/InputBase";
import CircularProgress from "@mui/material/CircularProgress";
import { InputAdornment } from "@mui/material";
import { useRouter } from "next/router";
import StocksJSON from "../../assets/stocks.json";

export const Search = styled("div")(({ theme }) => ({
  position: "relative",
  border: theme.shape.borderRadius,
  backgroundColor: alpha(theme.palette.common.white, 0),
  "&:hover": {
    backgroundColor: alpha(theme.palette.common.white, 0),
  },
  marginRight: theme.spacing(2),
  marginLeft: 0,
  width: 500,
  [theme.breakpoints.up("sm")]: {
    marginLeft: theme.spacing(3),
    width: 500,
  },
}));

export const StyledInputBase = styled(InputBase)(({ theme }) => ({
  color: "inherit",
  "& .MuiInputBase-input": {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)})`,
    transition: theme.transitions.create("width"),
    width: "100%",
    [theme.breakpoints.up("md")]: {
      width: "20ch",
    },
  },
}));

interface Stock {
  symbol: string;
  long_name: string;
  sector: string | null;
}

export default function SearchBar() {
  const [open, setOpen] = React.useState(false);
  const [options, setOptions] = React.useState<readonly Stock[]>([]);
  const loading = open && options.length === 0;
  const router = useRouter();

  const handleOptionSelection = (option: Stock) => {
    router.push("/stocks/" + option.symbol);
  };

  React.useEffect(() => {
    let active = true;

    if (!loading) {
      return undefined;
    }

    (async () => {
      if (active) {
        setOptions([...StocksJSON]);
      }
    })();

    return () => {
      active = false;
    };
  }, [loading]);

  React.useEffect(() => {
    if (!open) {
      setOptions([]);
    }
  }, [open]);

  return (
    <div>
      <Search>
        <Autocomplete
          id="asynchronous-demo"
          fullWidth
          autoComplete
          autoHighlight
          clearOnEscape
          clearOnBlur
          popupIcon={""}
          sx={{
            ".MuiOutlinedInput-notchedOutline": {
              color: alpha("#fff", 0.2),
              border: "none",
              borderBottom: 1,
              borderRadius: 0,
            },
          }}
          open={open}
          onOpen={() => {
            setOpen(true);
          }}
          onClose={() => {
            setOpen(false);
          }}
          isOptionEqualToValue={(option, value) =>
            option.symbol === value.symbol
          }
          getOptionLabel={(option) => option.symbol + " : " + option.long_name}
          options={options}
          loading={loading}
          onChange={(event, option) => option && handleOptionSelection(option)}
          renderInput={(params) => (
            <TextField
              {...params}
              placeholder="Search ASX:"
              InputProps={{
                ...params.InputProps,
                startAdornment: (
                  <InputAdornment position="start">
                    <SearchIcon />
                  </InputAdornment>
                ),
                endAdornment: (
                  <React.Fragment>
                    {loading ? (
                      <CircularProgress color="inherit" size={20} />
                    ) : null}
                    {params.InputProps.endAdornment}
                  </React.Fragment>
                ),
              }}
            />
          )}
        />
      </Search>
    </div>
  );
}
