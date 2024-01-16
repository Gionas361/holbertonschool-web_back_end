export default function returnHowManyArguments(...theArgs) {
  let args = 0;
  for (const i in theArgs) {
    args += 1 + (i - i);
  }
  return args;
}
