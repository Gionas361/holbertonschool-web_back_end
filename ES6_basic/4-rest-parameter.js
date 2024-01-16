export default function returnHowManyArguments(...theArgs) {
  let args = 0;
  for (const arg of theArgs) {
    args += 1;
  }
  return args;
}
