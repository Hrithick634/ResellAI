import { useState } from "react";
import axios from "axios";
import { BRAND_OPTIONS } from "./constants";

function App() {
  const [image, setImage] = useState(null);
  const [brand, setBrand] = useState("");
  const [ram, setRam] = useState("");
  const [storage, setStorage] = useState("");
  const [age, setAge] = useState("");
  const [mrp, setMrp] = useState("");
  const [backbody, setBackbody] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [preview, setPreview] = useState(null);

  const handleSubmit = async () => {
    if (
      !image ||
      !brand ||
      !ram ||
      !storage ||
      age === "" ||
      mrp === "" ||
      backbody === ""
    ) {
      alert("Please fill all fields");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);
    formData.append("brand", brand);
    formData.append("ram", ram);
    formData.append("storage", storage);
    formData.append("phone_age", age);      // bucketed value
    formData.append("mrp", mrp);
    formData.append("backbody", backbody);  // 0 or 1

    try {
      setLoading(true);
      const res = await axios.post(
        "http://127.0.0.1:8000/predict",
        formData
      );
      setResult(res.data);
      setPreview(null);
    } catch (err) {
      alert("Error while predicting");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "500px", margin: "auto" }}>
      <h2>Mobile Damage & Resale Estimator</h2>

      {/* Image upload */}
      <input
        type="file"
        accept="image/*"
        onChange={(e) => {
          const file = e.target.files[0];
          setImage(file);
          setPreview(URL.createObjectURL(file));
        }}
      />

      {preview && (
        <div style={{ marginTop: "10px" }}>
          <img
            src={preview}
            alt="Preview"
            style={{
              width: "100%",
              maxHeight: "300px",
              objectFit: "contain",
              border: "1px solid #ccc",
              borderRadius: "8px"
            }}
          />
        </div>
      )}

      <br /><br />

      {/* Brand */}
      <select value={brand} onChange={(e) => {
        setBrand(e.target.value);
        setRam("");
        setStorage("");
      }}>
        <option value="">Select Brand</option>
        {Object.keys(BRAND_OPTIONS).map(b => (
          <option key={b} value={b}>{b}</option>
        ))}
      </select>

      <br /><br />

      {/* RAM */}
      {brand && (
        <select value={ram} onChange={(e) => setRam(e.target.value)}>
          <option value="">Select RAM (GB)</option>
          {BRAND_OPTIONS[brand].ram.map(r => (
            <option key={r} value={r}>{r} GB</option>
          ))}
        </select>
      )}

      <br /><br />

      {/* Storage */}
      {brand && (
        <select value={storage} onChange={(e) => setStorage(e.target.value)}>
          <option value="">Select Storage</option>
          {BRAND_OPTIONS[brand].storage.map(s => (
            <option key={s} value={s}>
              {s >= 1024 ? `${s / 1024} TB` : `${s} GB`}
            </option>
          ))}
        </select>
      )}

      <br /><br />

      {/* Phone age bucket */}
      <select value={age} onChange={(e) => setAge(e.target.value)}>
        <option value="">Select Phone Age</option>
        <option value="1">&lt; 1 year</option>
        <option value="2">&lt; 2 years</option>
        <option value="3">&lt; 3 years</option>
        <option value="4">&lt; 4 years</option>
        <option value="5">&lt; 5 years</option>
        <option value="6">&gt; More than 5 years</option>
      </select>

      <br /><br />

      {/* Back body broken */}
      <select value={backbody} onChange={(e) => setBackbody(e.target.value)}>
        <option value="">Back Body Broken?</option>
        <option value="1">Yes</option>
        <option value="0">No</option>
      </select>

      <br /><br />

      {/* MRP */}
      <input
        type="number"
        placeholder="MRP (₹)"
        value={mrp}
        onChange={(e) => setMrp(e.target.value)}
      />

      <br /><br />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Processing..." : "Estimate Resale Value"}
      </button>

      <br /><br />

      {/* Result */}
      {result && (
        <div>
          <h3>Result</h3>

          {!result.screen_detected ? (
            <p style={{ color: "red" }}>
              ❌ Phone screen not detected. Please upload a clear front image.
            </p>
          ) : (
            <>
              <p>Damage Class: {result.damage_class}</p>
              <p>Damage Score: {result.damage_score}</p>
              <p>Spec Depreciation: {result.spec_depreciation}</p>
              <h2>Estimated Resale Value: ₹{result.resale_value}</h2>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
