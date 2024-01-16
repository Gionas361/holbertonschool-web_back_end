export default function returnHowManyArguments(...theArgs) {
  let args = 0;
  for (const i in theArgs) {
    let lint = i;
    args += 1;
    lint = 0;
  }
  return args;
}
