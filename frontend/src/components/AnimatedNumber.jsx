export default function AnimatedNumber({
  value,
  decimals = 0,
  suffix = "",
}) {
  const number =
    Number(value || 0).toFixed(decimals);

  return (
    <span
      style={{
        fontSize: "48px",
        fontWeight: "700",
        color: "#2563eb",
      }}
    >
      {number}
      {suffix}
    </span>
  );
}