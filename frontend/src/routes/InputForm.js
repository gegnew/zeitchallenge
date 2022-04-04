import { useState } from "react";
import {
  Box,
  Button,
  Center,
  Container,
  FormControl,
  FormLabel,
  Flex,
  Input,
  List,
  ListItem,
  Text,
  Tag,
  Heading,
} from "@chakra-ui/react";

const InputForm = () => {
  const [text, setText] = useState("");
  const [formField, setFormField] = useState([]);

  const handleFormChange = (event) => {
    setText(event.target.value);
  };

  const submit = (event) => {
    event.preventDefault();

    if (text === "") return;

    fetch("http://localhost:8000/api/v1/count", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: text }),
    })
      .then((response) => response.json())
      .then((data) => {
        setFormField([...formField, `${text}: ${JSON.stringify(data)}`]);
        setText("");
      })
      .catch((error) => {
        console.log(error);
        setText("");
      });
  };

  const clear = () => {
    setFormField([]);
  };

  return (
    <Flex minH={"100vh"} align={"center"} justify={"center"} bg={"gray.50"}>
      <Box rounded={"lg"} bg={"white"} boxShadow={"lg"} p="10">
        <FormControl onSubmit={submit}>
          <FormLabel htmlFor="inputtext">
            <Heading as="h4" size="sm">
              Count string:
            </Heading>
          </FormLabel>
          <Input
            mb={2}
            id="inputtext"
            type="text"
            placeholder="Enter Text"
            onChange={(event) => handleFormChange(event)}
            value={text}
            onKeyDown={(e) => e.key === "Enter" && submit(e)}
          />
          <Button
            md={2}
            onClick={submit}
            bg={"blue.400"}
            color={"white"}
            _hover={{
              bg: "blue.500",
            }}
          >
            Submit
          </Button>

          <Button mx={2} variant="outline" onClick={clear}>
            Clear
          </Button>
        </FormControl>
        <List>
          {formField.map((field, index) => (
            <ListItem my={2} key={index}>
              <Tag size="lg" variant="outline" colorScheme="blue">
                {field}
              </Tag>
            </ListItem>
          ))}
        </List>
        {formField.length === 0 && (
          <Text mt={2} color="gray.500" isTruncated>
            No input yet
          </Text>
        )}
      </Box>
    </Flex>
  );
};

export default InputForm;
