export const notBlank = () => {
  return (v) => {
    if (!v || !v.match(/\S/g)) {
      return "入力してください。";
    }

    return "";
  };
};

export const atLeast = (digit) => {
  return (v) => {
    if (v.length < digit) {
      return `${digit}文字以上で入力してください。`;
    }

    return "";
  };
};
